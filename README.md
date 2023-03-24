# House Of Paws

<!-- TABLE OF CONTENTS -->
<a name="readme-top"></a>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#intro">Intro</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#dependencies-instructions">Dependencies Instructions</a></li>
    <li><a href="#application-architecture">Application Architecture</a></li>
    <ul>
        <li><a href="#entity-relationship-diagram">Entity Relationship Diagram</a></li>
        <li><a href="#wireframes">Wireframes</a></li>
    </ul>
    <li><a href="#unsolved-problems">Unsolved Problems</a></li>
    <li><a href="#users-stories">Users Stories</a></li>
    <li><a href="#general-approach">General Approach</a></li>
    <li><a href="#overcoming-challenges">Overcoming Challenges</a></li>
    <li><a href="#future-enhancement">Future Enhancement</a></li>
  </ol>
</details>

## Intro

A website for a vet clinic named House Of Paws where users can book an appointment for available services on the website for their pets. 

## Technologies Used

[![HTML5](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)](https://en.wikipedia.org/wiki/HTML)

[![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)](https://en.wikipedia.org/wiki/CSS)

[![BootStrap5](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://www.getbootstrap.com)

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

[![JQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)](https://jquery.com/)

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)


## Dependencies Instructions

#### Django Crispy Form 

```
pip install django-crispy-form
```

#### Crispy BootStrap 5

```
pip install crispy-bootstrap5
```

## Application Architecture

### <ins>Entity Relationship Diagram</ins>

![ERD](https://i.imgur.com/P5SPJgp.jpg)

### <ins>Wireframes</ins>

![HomePage](https://i.imgur.com/CDftI3e.png)

## Unsolved Problems

- [ ] If user attempts to add an appointment without adding a pet it will throw an error.
- [ ] Fix Change Password so that it shows a success message when change password is successful.
- [ ] Adding an Overlay to Images in BootStrap
- [ ] Render two forms in one page when using Class Based Views (CBVs)

## Users Stories

Users are clients that have pets that need to book an appointment for specific care that their pet needs through the website. User needs to first register and add the pet they wish to take an appointment for and only then are they able to book an appointment. Clients can also add and see reviews individually for each service.

## General Approach

As a team, we first decided the best way to apporoach this project was to think of an idea for a website. Once we had figured that out we then focused on wireframes by drawing them on paper. Later we used [draw.io](draw.io) to make the Entity Relationship Diagram. To keep track of our progress and divide the work between each other we used [Trello](https://trello.com/).

## Overcoming Challenges

- Showing name of pets in the dropdown menu in the appointment form instead of it returning it as Pets Objects.
- Including reviews so that they would be tied to the individual service that the review was made for and it would also display the name of the user that made the review.

## Future Enhancement

- Have the ability to add mulitple vets that can offer different services in addition to the ones already added.
- Make the services more detailed. For example, specify what type of surgeries the vets can offer.
- Add a search bar. 

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>