# Application Examples DocSpace

This readme file is a specific guide for this feature branch only, it will be changed later.

## How to check result locally

- First step clone this package to your PC. Make sure you checkout the right feature branch
- After that you just need to click the sud_update.bat file, wait until on the command appear **"Starting suds-web server..."** with the green color
- Browse sud's local web link [http://localhost:8080/application-examples/1.0.0/](http://localhost:8080/application-examples/1.0.0/) by any browser and see the output

## Important notes

1. In this version we are using very simple DocspaceMenu, we use only Docleaf as menu item

    ```c
    <DocSpace Title>
    <DocLeafA Title>
        <DocLeafA Content>
        <DocLeafA Content>
    ```

    Feel free to give your suggestion  
    Some useful links for your reference  
    [DocspaceMenu](https://confluence.silabs.com/display/DocsDev/DocSpaceMenu)  
    [DocleafMenu](https://confluence.silabs.com/display/DocsDev/DocLeafMenu)

2. This is very draft version I tried to depict things as my understanding so don't put too much attention to the content of markdown files

3. I included batch file and even suds.exe to this package just for your convenience. It will be removed later

4. We are lacking permission for doing below things

    - Viewing the result on “Scratch” development AWS server. As I checked some Jenkins file of the other team it points to [http://qa-pre-review-docs.suds.silabs.net/](http://qa-pre-review-docs.suds.silabs.net/)
    - Creating release ticket, but not sure on TECHDOCS or TECHPUBS
