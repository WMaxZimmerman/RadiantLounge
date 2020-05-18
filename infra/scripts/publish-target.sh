targetDir=$1

cd site/RadiantLounge.Site.UI
dotnet restore
dotnet build
dotnet publish --configuration Release --output $targetDir
