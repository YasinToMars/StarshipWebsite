# StarshipWeb
**A website for the future** <br>
This is an inspiring website with the goal of giving latest news about SpaceX's Starship rocket to rocket nerds. <br>
### About websites:
There is a website for the user page, where the user can get the latest news about Starship or contact the website admin. <br>
**Link to the user website: [https://starshipweb.onrender.com*](https://starshipuserwebsite.onrender.com)* <br>
There is also a website for the admin. The admin can use that panel to see who wants to contact them. <br> 
**Link to the admin website: https://starshipwebsite-1z5w.onrender.com*

# User Website
### HomePage:
The homepage is were it inspires everyone! It contains a beautiful video of Super Heavy catch in the background. 
![Screenshot 2025-01-14 at 9 30 03 AM](https://github.com/user-attachments/assets/3e16e6b5-acc8-487b-b71b-be626f53806f)


### SideBar:
In the sidebar, there are 4 different buttons, and each button takes you to a separate page. 
![Screenshot 2025-01-14 at 9 30 58 AM](https://github.com/user-attachments/assets/b89e5f38-eb35-4046-b484-d899aef830f0)

### Page 1: Latest News 
In this page, the usser can find the latest news about Starship. 

*![Screenshot 2025-01-14 at 9 33 27 AM](https://github.com/user-attachments/assets/05e69a86-2375-4d28-8d6e-2352bc92ec27)
The image used in the background of this page is from SpaceX*

### Page 2 Multi-Cam:
In this page, the user can see multiple live camera feeds (from YouTube) of Starbase texas. 
![Screenshot 2025-01-14 at 9 55 04 AM](https://github.com/user-attachments/assets/9c23143f-ff78-4184-8659-6a046773066c)


### Page 3: Road Closures 
In this page, the user can see the schedule for road closures (HW4 at Starbase). The closures are loaded from a databse (`closures.db` file).
![Screenshot 2025-01-14 at 9 34 45 AM](https://github.com/user-attachments/assets/bdf82953-96d3-4a49-b105-fa0095469711)

### Page 4: Contact Us
In this page the user can contact the website's admin. The user can enter their name, email and their message. These infos (name, email and message) will be dumped into a PostgreSQL databse.
![Screenshot 2025-01-14 at 9 40 29 AM](https://github.com/user-attachments/assets/3d86b5e6-4b5e-4df2-ad64-bd42b673e973)


# Admin Website:
This website has only one page, showing the messages (including their Email and Name) sent by the user. The datas are being loaded from the database. 
![Screenshot 2025-01-14 at 9 57 33 AM](https://github.com/user-attachments/assets/28883ccf-58bf-48b4-b5c3-24de21eb5b0d)


# How does the database creation work? 
The PostgreSql database will be created in render.com <br> 
Using the `psql` command (with the external database URL) we can connect to the database. We enter the SQL Table creation command to create a table:
```CREATE TABLE contact (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
