ArgoCD
### we will be doing the automation with argoCD with the following steps
kubectl create ns devops-labs
helm repo add argo https://argoproj.github.io/argo-helm
kubectl create namespace argocd
helm install argocd argo/argo-cd -n argocd
kubectl edit svc argocd-server // change this to NodePort
kubectl get secret argocd-initial-admin-secret -n argocd \
  -o jsonpath="{.data.password}" | base64 -d && echo
# login to browser with admin and the password that you get from above
kubectl apply -f app-deploy.yaml

FluxCD
### we will be doing the automation with fluxCD with the following steps
# https://fluxcd.io/flux/installation/
brew install fluxcd/tap/flux
. <(flux completion zsh)
# https://fluxcd.io/flux/installation/bootstrap/generic-git-server/
# https://github.com/settings/tokens 
export GITHUB_TOKEN=<> 
export GITHUB_USER=syednadeembe
flux bootstrap github --owner=$GITHUB_USER --repository=syednadeembe/sre-repo --branch=main --path=. --personal
flux get kustomization
