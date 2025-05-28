# Setting up EKS Access from EC2 Bastion Host

This guide walks through setting up Amazon EKS cluster access from an EC2 bastion host, including VPC configuration, IAM roles, and kubectl setup.

## Prerequisites

- AWS Account with appropriate permissions
- Basic understanding of VPC, IAM, and EKS concepts
- AWS CLI configured (optional but recommended)

## Architecture Overview

This setup creates:
- A VPC with public and private subnets
- An EKS cluster in private subnets
- A bastion host in public subnet for secure access
- Proper IAM roles and security group configurations

## Step-by-Step Implementation

### Step 1: Create VPC

Create a VPC where you want to deploy your EKS cluster.

**Requirements:**
- Public subnets for bastion host and NAT gateway
- Private subnets for EKS worker nodes
- Internet Gateway and NAT Gateway for connectivity

![image](https://github.com/user-attachments/assets/a67677a6-f94f-4f7c-bb35-b1a8e50f5c95)


### Step 2: Create EKS Service Role

Create an IAM role that allows the EKS control plane to manage AWS resources on your behalf.

1. Go to **IAM Console** → **Roles** → **Create role**
2. Select **AWS Service** → **EKS** → **EKS - Cluster**
3. Attach the following managed policies:
   - `AmazonEKSClusterPolicy`
4. Name the role (e.g., `eks-cluster-role`)
5. Create the role

![EKS Role Creation Step 1](screenshots/eks-role-step1.png)
![EKS Role Creation Step 2](screenshots/eks-role-step2.png)
![EKS Role Creation Step 3](screenshots/eks-role-step3.png)

### Step 3: Create EKS Cluster

1. Navigate to **EKS Console** → **Create cluster**
2. **Cluster Configuration:**
   - Name: `my-eks` (or your preferred name)
   - Kubernetes version: Latest stable
   - Service role: Select the role created in Step 2

3. **Networking:**
   - VPC: Select your VPC from Step 1
   - Subnets: Choose **private subnets** only
   - Security groups: Default EKS security group
   - Endpoint access: 
     - Public access: Enabled
     - Private access: Enabled
     - Description: "The cluster endpoint is accessible from outside of your VPC. Worker node traffic to the endpoint will stay within your VPC."

4. **Access Configuration:**
   - Authentication mode: API and ConfigMap
   - Allow cluster administrator access for your IAM principal

5. Click **Next** → **Next** → **Create**

6. **Copy the cluster ARN** for later use:
   ```
   arn:aws:eks:ap-south-1:267714372222:cluster/my-eks
   ```

![EKS Cluster Creation](screenshots/eks-cluster-creation.png)
![EKS Networking Configuration](screenshots/eks-networking-config.png)
![EKS Access Configuration](screenshots/eks-access-config.png)

### Step 4: Create IAM Role for Bastion Host

Create an IAM role for the EC2 bastion host to access EKS cluster.

1. Go to **IAM Console** → **Roles** → **Create role**
2. Select **AWS Service** → **EC2**
3. Attach the following managed policies:
   - `AmazonEKSWorkerNodePolicy`
   - `AmazonEKS_CNI_Policy` 
   - `AmazonEC2ContainerRegistryReadOnly`
   - Or create a custom policy with necessary EKS permissions
4. Name the role: `bastion-eks-access-role`
5. Create the role

![Bastion IAM Role Creation Step 1](screenshots/bastion-role-step1.png)
![Bastion IAM Role Creation Step 2](screenshots/bastion-role-step2.png)
![Bastion IAM Role Creation Step 3](screenshots/bastion-role-step3.png)

### Step 5: Launch Bastion Host

1. Go to **EC2 Console** → **Launch Instance**
2. **Configuration:**
   - AMI: Amazon Linux 2 or Ubuntu
   - Instance type: t3.micro (or as needed)
   - VPC: Same VPC as EKS cluster
   - Subnet: **Public subnet**
   - Auto-assign public IP: **Enable**
   - Security group: Allow SSH (port 22) from your IP
   - IAM role: `bastion-eks-access-role`

3. Launch the instance

![EC2 Bastion Host Configuration](screenshots/bastion-host-config.png)
![Bastion Host IAM Role Assignment](screenshots/bastion-role-assignment.png)

### Step 6: Install kubectl on Bastion Host

SSH into your bastion host and install kubectl:

```bash
# Download kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Make it executable
chmod +x kubectl

# Move to system path
sudo mv kubectl /usr/local/bin/

# Verify installation
kubectl version --client
```

![kubectl Installation Error](screenshots/kubectl-connection-error.png)
*Initial connection will fail - this is expected and will be resolved in the following steps.*

### Step 7: Configure EKS Security Group

Allow the bastion host to communicate with the EKS cluster by updating the EKS security group.

1. Go to **EC2 Console** → **Security Groups**
2. Find the EKS cluster security group
3. **Add Inbound Rule:**
   - Type: All traffic (or specific ports as needed)
   - Source: VPC CIDR block (e.g., 10.0.0.0/16)

![EKS Security Group Configuration](screenshots/eks-security-group.png)
![VPC CIDR Configuration](screenshots/vpc-cidr.png)
![Security Group Rules](screenshots/security-group-rules.png)

### Step 8: Update AWS Auth ConfigMap

⚠️ **Important:** This step must be performed from your AWS account that created the EKS cluster (use CloudShell or local AWS CLI).

1. **Create the ConfigMap YAML file:**

```yaml
# auth-aws.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
data:
  mapRoles: |
    - rolearn: arn:aws:iam::267714372222:role/bastion-eks-access-role
      groups:
        - system:masters
```

2. **Apply the ConfigMap:**

```bash
# First, configure kubectl to connect to your EKS cluster
aws eks update-kubeconfig --region ap-south-1 --name my-eks

# Apply the aws-auth ConfigMap
kubectl apply -f auth-aws.yaml
```

![CloudShell ConfigMap Creation](screenshots/configmap-creation.png)

### Step 9: Configure kubectl on Bastion Host

On the bastion host, configure kubectl to connect to your EKS cluster:

```bash
# Configure kubectl
aws eks update-kubeconfig --region ap-south-1 --name my-eks

# Test the connection
kubectl get nodes
kubectl get pods --all-namespaces
```

> 📸 **Screenshot needed:** Successful kubectl commands from bastion host

## Verification

After completing all steps, you should be able to:

1. SSH into the bastion host
2. Run `kubectl` commands successfully
3. View cluster nodes and pods
4. Deploy applications to the EKS cluster

## Troubleshooting

### Common Issues:

1. **"error: You must be logged in to the server (Unauthorized)"**
   - Verify the aws-auth ConfigMap is correctly applied
   - Ensure the bastion host IAM role ARN matches in the ConfigMap

2. **Connection timeout**
   - Check EKS security group allows traffic from VPC CIDR
   - Verify bastion host is in public subnet with internet access

3. **kubectl command not found**
   - Reinstall kubectl following Step 6

## Security Considerations

- Bastion host should only allow SSH from trusted IP addresses
- Use session manager instead of SSH for enhanced security
- Regularly rotate IAM credentials
- Monitor bastion host access logs
- Consider using AWS Systems Manager Session Manager

## Clean Up

To avoid charges, remember to delete:
1. EKS cluster
2. EC2 bastion host
3. NAT Gateway
4. Elastic IPs
5. VPC (if no longer needed)

## References

- [Amazon EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/)
- [Managing users or IAM roles for your cluster](https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html)
- [kubectl installation guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

---

**Note:** Replace account IDs, region names, and resource ARNs with your actual values.





