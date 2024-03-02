# we will be doing the automation with fluxCD
# https://fluxcd.io/flux/installation/
brew install fluxcd/tap/flux
. <(flux completion zsh)
# https://fluxcd.io/flux/installation/bootstrap/generic-git-server/
# https://github.com/settings/tokens 

export GITHUB_TOKEN=<> 
export GITHUB_USER=syednadeembe

flux bootstrap github --owner=$GITHUB_USER --repository=syednadeembe/sre-repo --branch=main --path=. --personal

flux get kustomization