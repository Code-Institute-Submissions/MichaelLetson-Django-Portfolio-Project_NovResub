# The PT App 

![image](https://user-images.githubusercontent.com/93741957/183312827-df3ec622-d16a-4b32-87db-7d734da47504.png)

## Purpose & Features
The purpose of this site is to help Personal Trainers become more accessible, to help PTs promote themselves and gain clientel with more ease than resources that are currently available. This site helps answer the question, where do I find a new Personal Trainer without searching social mdeia platforms and not through word of mouth? And gives new, more junior PTs a great platform to expose themselves to potential clients - whilst also adding benefit to more experienced PTs to further grow their client pool.

#### Features 
The user has the ability to log in or register to become a member, which allows them to edit, delete or create posts for a PT.

### Colour Theme

![image](https://user-images.githubusercontent.com/93741957/183293877-0c8a89e6-146d-46b9-bc06-6a279ad770d6.png)

I took this colour scheme from https://designshack.net/articles/trends/best-website-color-schemes/ - I found it worked well and added a good look to a sporty webpage. 

### What is the app?

This app is to provide visibility of PTs to people who are in search of a PT. 

### Why? 
Sounds like a simple website, but currently, unless you know someone or are willing to approach people in the gym or to search social media apps, it's difficult to find a Personal Trainer. This website makes the solution simple, "check the PT App".

### Who is the target audience? 
Either PTs wanting to sell themselves to gain clients, or people looking for a PT.

## Struggles

Some key struggles I came across were the forms in this page. What I had initially planned to do was beyond the scope of what had been taught in this projects resources. Unbenounced to the complexities of uploading images that would display on the site, having forms that could be displayed with prefilled detail that could be edited and the planning of the infrastructure behind this - I managed to overcome this through my own research, thankfully. 

The issue of uploading an image, and storing images in cloudinary that could be displayed, this issue was very difficult to overcome and was not directly disucssed in related walkthrough videos I had been working from, I did not have enough time to self-teach the process of doing this, so decided to remove the functionality to upload your own photo, and used a code institute provided link for an image which will be used in the site. This image is non-related to the context of the site, which is why I am highlighting the reason for using that image here. 

I also struggled with linking up and creating unit tests. This is something I was very keen on, and the walkthrough videos did not give good insight into how to write unit tests inside Django. 

## Expansion & Improvements

There is definitely room to improve and expand upon this site, the aforementioned image used for the posts could be relative to working out or the gym.
To expand on the site would be to add more functionality, like contacting the PTs via the post, or post detail page. 
I would also add extra features like gym locations, cheaper gym prices, workout program templates for members to use, nuitritional advice/plans...basically anything PT or gym related to help consolidate one place for all information. 

## Testing

Throughout this development I was manually testing the functionality, UI/UX, user stories and more. After each body of work I had done for a feature or styling, I manually tested, I tried using different browsers, strain testing, thinking of edge cases in a continuous cycle from start to finish during development. 

### PEP8

Did PEP8 checks on key files and had to edit spacing in settings.py, forms.py, models.py and urls.py to make all pass okay. These are the key files I checked via http://pep8online.com/. 

### HTML Validator

![image](https://user-images.githubusercontent.com/93741957/183312352-40f975f7-f7ac-4a4d-b2de-9b9aad999e7a.png)

Only two issues found, both were rectified and code added and committed. Checked via https://validator.w3.org/ 

### CSS Validator

![image](https://user-images.githubusercontent.com/93741957/183312418-1eccb024-b34a-40c2-a407-c7490df18a2e.png)

No issues found in validator check for CSS, checked via https://jigsaw.w3.org/css-validator/ 

### Lighthouse

![image](https://user-images.githubusercontent.com/93741957/183272043-03abe835-7d75-4ed4-8172-0a407619759d.png)

Lighthouse report shows really good results. After initially running this report, it brought to light missing 'alt' tags in the <img> tags across the sight.
The performance result is very poor, but after using code institute template, and following all require steps by following the provided walkthrough videos, I am unsure as to the result being so low. Also to debug and try and improve upon this, is something that is out of the remit of this project and was not taught. 

## Deployment 

This project was deployed via Heroku.

- Login to Heroku account on app.
- Set buildbacks to Django and Cloudinary. 
- Link Heroku to Git repository.
- Deployed.

## Using Git 

I created a respository and opened in gitpod to create my code. To move my code from gitpod to repository ready for deployment I followed these steps (which I did often to show a journey of creating my site):

- git add .
- git commit -m "message"
- git push
- git pull --rebase

## Tools

### To Do
![image](https://user-images.githubusercontent.com/93741957/183296206-eeda935a-3581-4fb5-82a1-048d571d0bea.png)

I used To Do to try and follow somewhat of a Kanban approach to completing this project, I have unticked each for visibility within README.

### Flowchart 
![image](https://user-images.githubusercontent.com/93741957/183296269-33b7064a-9153-4302-b4c2-3444e8e62f41.png)

This is the flowchart I had created for the flow when landing on the website, simple steps of viewing more detail, creating a new post, or edit/deleting a post all divided up based on whether the user is authenticated or not. 

### Resources 

For resources not mentioned above, I used Slack, Google, YouTube, Code Institute walkthrough videos and tutoring as well as relate tech stack documentation. All to help with developing and debugging across the site. 
