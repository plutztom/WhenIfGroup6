CREATE TABLE Courses (
        Course_Name       VARCHAR2(100),
        Course_ID         NUMBER  PRIMARY KEY,
        Units             NUMBER,
        Department_ID     NUMBER,
        People_Soft_ID    NUMBER,
        Description       VARCHAR2(1000),   
        Term_Offered      VARCHAR2(100),
        CONSTRAINT ck_trm     CHECK(term_offered IN ('Autumn', 'Winter', 'Spring', 'Summer')),
        --check term in fall, winter, spring, summer
        Class_type        VARCHAR2(100),
        CONSTRAINT ck_class   CHECK(Class_type IN ('In-Class', 'Online', 'Distance Learning', 'DL'))
        --check type in-class or online
        
      );
      
      
      CREATE TABLE Programs (
        Program_ID        NUMBER PRIMARY KEY,
        Program_Name      VARCHAR2(100),
        Course            NUMBER, FOREIGN KEY (Course) REFERENCES Courses(Course_ID)
        
        );
        
        CREATE TABLE Students (
        Student_ID        NUMBER PRIMARY KEY,
        First_Name        VARCHAR2(300),
        Last_Name         VARCHAR2(300),
        Status            VARCHAR2(100),
        --check in active, graduated, frozen
        Term_Start        DATE,
        Term_End          DATE,
        People_Soft_ID    NUMBER,
        FOREIGN KEY (People_Soft_ID) REFERENCES Users(People_Soft_ID),
        DOB               DATE,
        Phone             NUMBER,
        Email             VARCHAR2(300),
        Address           VARCHAR2(300)
        );
        
        CREATE TABLE Faculty (
        Faculty_ID        NUMBER PRIMARY KEY,
        People_Soft_ID    NUMBER, 
        FOREIGN KEY (People_Soft_ID) REFERENCES Users(People_Soft_ID),
        First_Name        VARCHAR2(300),
        Last_Name         VARCHAR2(300),
        Job_Title         VARCHAR2(100)
        );
        
        CREATE TABLE Users (

        User_id                 NUMBER,
        Password                VARCHAR2(20),
        People_Soft_ID          NUMBER PRIMARY KEY NOT NULL,
        Last_Successful_Login   DATE
        );
