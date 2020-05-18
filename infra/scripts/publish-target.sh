targetDir=$1

cd src/RadiantLounge.Site.UI
dotnet restore
dotnet build
dotnet publish --configuration Release --output $targetDir
