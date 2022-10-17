# HACKTOBER FIESTA - 22

## Prerequisites
- Sign up to [Hacktoberfest 2022](https://hacktoberfest.digitalocean.com/)
- Have a photo of yours ready in 1:1 ratio. To make it in 1:1 ratio edit the photo and select the crop icon. From there select the square icon, this ensures your photo is in 1:1 ratio.
-  Install [VsCode](https://code.visualstudio.com/download), [NodeJs](https://nodejs.org/en/download/), [Git](https://git-scm.com/downloads) and have an account in [Github](https://github.com/)
- Have python and pip installed on your system

<br>

## Note
- Create a new pull request, only after the previous one is accepted

<br>

## Setup

### Step 1 - Fork
As the first step, you have to `fork` this repository to your own github account. 
For that please click on the fork button on the top right corner of your window.  
You will now have the forked repository among your own repositories.    
![Fork](https://github.com/dkowsikpai/card/blob/main/Screenshots/fork.png)
<br>

### Step 2 - Clone 
Clone the repository to your local machine using the git command.
```
git clone <url_to_forked_repository>
```

<br>

### Step 3 - Changing working directory
This will change the working directory to the newly cloned repository. 
```
  cd HACKTOBER-FIESTA22/
```

<br>

### Step 4 - Install Requirements

For ```portfolio```, Use npm to install modules. 
```
cd portfolio/
npm install
```

For ```pygame``` ,Use pip to install packages

```
cd pygame/
pip install -r requirements.txt
```

Note : Run the commands from ```HACKTOBER-FIESTA22``` folder

<br>

### Step 5 - Run the application
For ```portfolio```, The application can be run using the command. The application will be running at `localhost:3000` by default.
```
cd portfolio/
npm run dev
```

For ```pygame```, Run the python script

```
cd pygame/
python main.py
```

<br>

## Tasks

### PR 1 - Create your pygame

1. Create a ```username.py``` file in the ```pygame/gameit``` folder. You can create your game in this file. An example game is given in the ```example.py``` file inside the same folder provided.

Some ideas for games are - 

* Flappy Bird
* Snake Game 
* Retro Racing Game
* Sudoku Games 

Make sure that the game created is a callable function like the one in  ```example.py```,


2. Import your game function in ```pygame/main.py``` and add the function to ```games``` mapping

```
from gameit.username import functionName

....

games = {
    'example':exampleGame
    ...
    ...
    'username':functionName # add like this
}

```

<br>

### Intial Commit 
You can check your change using the following command

```
 git status
```
this command will show you the changes that you have made and left untracked, you have to add these changes to the staging area.

<br> 
Now, you should add it to the staging area using the following command.

```
  git add .
```
`.` specifies to add all the chnges to the staging area.
<br>
Now that the changes are tracked or added to the staging area you should make a commit regarding that particular change using the following command in the terminal. 

```
  git commit -m "<commit message>" 
```
The `commit message` message should specify what is the change made for, it will result in well documentation of the project

<br><br>

### Pushing the commit

Now that you have commited your changes you should push the changes to the remote git repository for that you can use the following command, given below

```
  git push -u origin main
```
This will automatically push your commit to the remote repository, it may ask your password / passphrase for authentication.


<br><br>

### Your Initial Pull Request(PR)
- Push your changes to the github repository.
- Go To Pull requests tab on github
- Click on `New Pull Request` button. 
- Make sure that head repository is your repository
![Pull Request Head](https://github.com/dkowsikpai/card/blob/main/Screenshots/PR%20Head.png)
- Make sure it is showing green tick mark
- Press on `Create Pull Request` Button
![Create PR](https://github.com/dkowsikpai/card/blob/main/Screenshots/Create%20PR.png)
- Add necessary title and description
- Hit `Create Pull Request` Button

<br>

### PR 2 - Document your pygame project

Create basic level documentation for your pygame created in ```username.py``` and make another pull request using the above given steps.

<br>



### PR 3 - Customize your Portfolio
- Change directory to ```portfolio``` using ```cd portfolio```
- Create a copy of the Template folder inside the component folder and rename it as `<your_github_username>`
- Inside the pages folder, create a copy of the `index.js` file and rename it as `<your_github_username>.js`
- Rename your image as `<your_github_username>` and add to the public folder
- Open ```/components/<your_github_username>/Navbar/Navbar.js```
- Goto line no:50, replace the image with ```src=/<your_image_file_name>```
- Goto `pages/<your_github_username>.js`, replace the Template folder name with `<your_github_username>`
    <br/>

  ```
  import EntryComponent from "../components/<your_github_username>/EntryComponent";
  ```
- Goto `component/<your_github_username>/EntryComponent.js`
- Replace image file name with your `<your_image_file_name>` 
    <br/>

  ```
  import ProfileImg from '../../public/<your_image_file_name>'
  ```
- From line 34, Customize the Hero section 
- After the changes are done, make another pull request using the above given steps.

<br>

### PR 4 - Add pygame project to your project list
- Go to `component/<your_github_username>/EntryComponent.js`, Edit your project with your pygame project details
<br/>

  ```
                      {/* Project 1 */}
                    <Grid sm={12} md={5} className="flex justify-center">
                        <Card css={{ width: "330px" }}>
                        <Card.Header>
                            <Text b> <Project_name> </Text>
                        </Card.Header>
                        <Card.Divider />
                        <Card.Body css={{ py: "$10" }}>
                            <Text>
                               <Project description in one sentence> 
                            </Text>
                        </Card.Body>
                        <Card.Divider />
                        <Card.Footer>
                            <Row justify="flex-end">
                                <Link href="<Project_repo_link>">
                                    <Button size="sm" light color="primary">Link</Button>
                                </Link>
                            </Row>
                        </Card.Footer>
                        </Card>
                    </Grid>
  ```
- Going to the url `localhost:3000/<github-username>` will now give you the sample portfolio.
- And you're all done.

<br>

