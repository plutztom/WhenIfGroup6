#Class Table definition plus some graduate course listings. -INCOMPLETE-
#Have to update the table definitions to fit more information - pre-reqs, term_offered, incompletes on drive
#Tuples contain courses which may then be inserted to db at once when db file is correct

'''CREATE TABLE  if not exists courses(
       course_name TEXT,
       course_id TEXT PRIMARY KEY,
       units INTEGER,
       department_id INTEGER,
       people_soft_id INTEGER,
       description TEXT,
       term_offered TEXT,
       CONSTRAINT ck_term CHECK(term_offered IN ('Autumn' OR 'Fall' , 'Winter', 'Spring', 'Summer')),
       class_type text,
       CONSTRAINT ck_class CHECK(class_type IN ('In-Class', 'Online', 'Distance Learning', 'DL')),
       ); '''
CNS_courses = [
    ('Introduction to Host Security', 'CNS418', ?, ?, ?, ?, 'Spring' 'Winter', 'In-Class' 'Online')
    ('Information Security Management', 'CNS440', ?, ?, ?, ?, 'Spring' 'Winter' 'Fall', 'In-Class' 'Online')
    ('Digital Forensic Techniques', 'CNS450', ?, ?, ?, ?, 'Fall', 'In-Class' 'Online')
    ('Physical and IT Security Convergence', 'CNS455', ?, ?, ?, ?, 'Winter', 'In-Class' 'Online')
    ('Critical Infrastructure and Control Systems Cybersecurity', 'CNS466', ?, ?, ?, ?, 'Spring', 'In-Class' 'Online')
    ('Legal Issues in Information Assurance', 'CNS477', ?, ?, ?, ?, 'Winter' 'Fall', 'In-Class' 'Online')
    ('Security Testing and Assessment', 'CNS488', ?, ?, ?, ?, 'Spring' 'Fall', 'In-Class' 'Online')
    ('Advanced Cyber Attack Responses and Defenses', 'CNS489', ?, ?, ?, ?, 'Fall', 'In-Class')
    ('Information Security Risk Assessment for Non-Profit Organizations', 'CNS490', ?, ?, ?, ?, 'Spring', 'In-Class')
    ('Enterprise Security Infrastructure Controls and Regulatory Compliance', 'CNS533', ?,?,?,?, 'Fall', 'In-Class' 'Online')
    ('Information Security Governance', 'CNS587', ?,?,?,?, 'N/A', 'N/A')
    ('Computer Information and Network Security Capstone', 'CNS594', ?,?,?,?, 'Spring' 'Winter', 'In-Class' 'Online')
    ('Topics in Computer Information and Network Security', 'CNS597', ?, ?, ?, ?, 'N/A', 'N/A')
    ('Independent Study', 'CNS599', ?,?,?,?, 'Fall', 'In-Class')
    ]
    
#edit table def for 'As Needed', 'N/A' , 'Every Other Academic Year' in term_offered constraint
CSC_courses = [
    ('Discrete Structures for COmputer Science', 'CSC400', ?, ?, ?, ?, 'Fall' 'Winter' 'Spring' 'Summer', 'In-Class' 'Online')
    ('Introduction to Programminig', 'CSC401', ?,?,?,?, 'Fall' 'Winter' 'Spring' 'Summer', 'In-Class' 'Online')
    ('Data Structures I', 'CSC402', ?,?,?,?, 'Fall' 'Winter' 'Spring' 'Summer', 'In-Class' 'Online')
    ('Data Structures II', 'CSC403', ?,?,?,?, 'Fall' 'Winter' 'Spring' 'Summer', 'In-Class' 'Online')
    ('Accelerated C++', 'CSC404', ?,?,?,?, 'Autumn' 'Winter' 'Spring', 'In-Class' 'Online')
    ('Systems I', 'CSC406', ?,?,?,?, 'Fall' 'Winter' 'Spring' 'Summer', 'In-Class' 'Online')
    ('Systems II', 'CSC407', ?,?,?,?, 'Fall' 'Winter' 'Spring' 'Summer', 'In-Class' 'Online')
    ('Tools and Techniques for Computational Analysis', 'CSC412', ?,?,?,?, 'Autumn' 'Winter', 'In-Class' 'Online')
    ('Applied Algorithms and Structures', 'CSC421', ?,?,?,?, 'Fall' 'Winter' 'Spring', 'In-Class' 'Online')
    ('Data Analysis and Regression', 'CSC423', ?,?,?,?, 'Fall' 'Winter' 'Spring' 'Summer2', 'In-Class' 'Online')
    ('Advanced Data Analysis', 'CSC424', ?,?,?,?, 'Fall' 'Winter' 'Spring' 'Summer', 'In-Class' 'Online')
    ('Time Series Analysis and Forecasting', 'CSC425', ?,?,?,?, 'Fall' 'Winter', 'In-Class' 'Online')
    ('Research Methods and Practice in Computing', 'CSC426', ?,?,?,?, 'Spring', 'In-Class' 'Online')
    ('Data Analysis for Experimenters', 'CSC428', ?,?,?,?, 'N/A', 'In-Class')
    ('Scientific Computing', 'CSC431', ?,?,?,?, 'Winter', 'In-Class' 'Online')
    ('Scripting for Data Analysis', 'CSC433', ?,?,?,?,'Spring', 'In-Class' 'Online')
    ('Distributed Systems I', 'CSC435', ?,?,?,?, 'Fall' 'Winter' 'Spring', 'In-Class' 'Online')
    ('Web Applications', 'CSC436', ?,?,?,?, 'Fall', 'In-Class' 'Online')
    ('Framework for Web Application Development', 'CSC438', ?,?,?,?, 'Spring', 'In-Class' 'Online')
    ('Computer Security', 'CSC439', ?,?,?,?, 'As Needed', 'In-Class' 'Online')
    ('Cryptology', 'CSC440', ?,?,?,?, 'Winter', 'In-Class' 'Online')
    ('Introduction to Operating Systems', 'CSC443', ?,?,?,?, 'Winter', 'In-Class' 'Online')
    ('Automate Theory and Formal Grammars', 'CSC444', ?,?,?,?, 'As Needed', 'In-Class' 'Online')
    ('Concepts of Programmiing Languages', 'CSC447', ?,?,?,?, 'Fall' 'Winter' 'Spring', 'In-Class' 'Online')
    ('Compiler Design', 'CSC448', ?,?,?,?, 'As Needed', 'In-Class' 'Online')
    ('Database Design', 'CSC451', ?,?,?,?, 'Fall' 'Winter' 'Spring' 'Summer', 'In-Class' 'Online')
    ('Database Programming', 'CSC452', ?,?,?,?, 'Fall' 'Winter' 'Spring' 'Summer', 'In-Class' 'Online')
    ('Database Technologies', 'CSC453', ?,?,?,?, 'Fall' 'Winter' 'Spring', 'In-Class' 'Online')
    ('Database Administration and Management', 'CSC454', ?,?,?,?, 'Winter' 'Summer', 'In-Class' 'Online')
    ('Database Processing for Large-Scale Analytics', 'CSC455', ?,?,?,?, 'Fall' 'Winter' 'Spring', 'In-Class' 'Online')
    ('Expert Systems', 'CSC457', ?,?,?,?, 'N/A', 'In-Class')
    ('Symbolic Programming', 'CSC458', ?,?,?,?, 'Every other Academic Year', 'In-Class' 'Online')
    ('Optimized C++', 'CSC461', ?,?,?,?, 'Fall' 'Spring', 'In-Class' 'Online')
    ('C++ Multithreading', 'CSC462', ?,?,?,?, 'Spring', 'In-Class' 'Online')
    ('Data Visualization', 'CSC465', ?,?,?,?, 'Fall' 'Winter' 'Spring', 'In-Class' 'Online')
    ('Mobile Application Development for iOS', 'CSC471', ?,?,?,?, 'Winter', 'In-Class' 'Online')
    ('Mobile Application Development for Android', 'CSC472', ?,?,?,?, 'Fall', 'In-Class' 'Online')
    ('Introduction to Robotics', 'CSC475', ?,?,?,?, 'N/A', 'In-Class')
    ('Programming Machine Learning Applications', 'CSC478', ?,?,?,?, 'Fall' 'Spring', 'In-Class' 'Online')
    ('Artificial Intelligence I', 'CSC480', ?,?,?,?, 'Winter', 'In-Class' 'Online')
    ('Introduction to Image Processing', 'CSC481', ?,?,?,?, 'Fall', 'In-Class' 'Online')
    ('Applied Image Analysis', 'CSC482', ?,?,?,?, 'Winter', 'In-Class' 'Online')
    ('Numerical Analysis', 'CSC485', ?,?,?,?, 'N/A', 'In-Class' 'Online')
    ('Theory of Computation', 'CSC489', ?,?,?,?, 'Fall', 'In-Class' 'Online')
    ('Mobile Application Development for iOS II', 'CSC491', ?,?,?,?, 'Spring', 'In-Class' 'Online')
    ('Mobile Application Development for Android II', 'CSC492', ?,?,?,?, 'N/A', 'In-Class' 'Online')
    ('Social Network Analysis', 'CSC495', ?,?,?,?, ('Fall', 'Spring'), ('In-Class','Online'))
    ('Research Colloquium', 'CSC500', ?,?,?,?, ('Fall', 'Winter', 'Spring'), ('In-Class' 'Online'))
    ('Parallel Algorithms', 'CSC503', ?,?,?,?, ('Winter'), ('In-Class' 'Online'))
    ('Monte Carlo Algorithms', 'CSC521', ?,?,?,?, ('Spring'), ('In-Class' 'Online'))
    ('Combinatorial Optimization', 'CSC525', ?,?,?,?, ('Winter'), ('In-Class' 'Online'))
    ('Computer Vision', 'CSC528', ?,?,?,?, ('As Needed'), ('In-Class' 'Online'))
    ('Advanced Data Mining', 'CSC529', ?,?,?,?, ('Fall', 'Winter', 'Spring'), ('In-Class' 'Online'))
    ('Introduction to Bioinformatics', 'CSC531', ?,?,?,?, ('Spring'), ('In-Class' 'Online'))
    ('Software Development for Limited and Embedded Devices', 'CSC534', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Formal Semantics of Programming Languages', 'CSC535', ?,?,?,?, ('As Needed'), ('In-Class' 'Online'))
    ('Distributed Systems II', 'CSC536', ?,?,?,?, ('Spring'), ('In-Class' 'Online'))
    ('Vision Systems', 'CSC538', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Mobile Application Development II', 'CSC540', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Spatial Databases and Geographic Information Systems', 'CSC543', ?,?,?,?, ('Spring'), ('In-Class' 'Online'))
    ('Advanced Topics in Programming Languages', 'CSC547', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Advanced Compiler Design', 'CSC548', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Database System Implementation', 'CSC549', ?,?,?,?, ('Fall'), ('In-Class' 'Online'))
    ('Object-Oriented Databases', 'CSC550', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Distributed Database Systems', 'CSC551', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Concurrent Software Development', 'CSC552', ?,?,?,?, ('Fall'), ('In-Class' 'Online'))
    ('Advanced Database Concepts', 'CSC553', ?,?,?,?, ('Winter'), ('In-Class' 'Online'))
    ('Advanced Database Management', 'CSC554', ?,?,?,?, ('Winter'), ('In-Class' 'Online'))
    ('Mining Big Data', 'CSC555', ?,?,?,?, ('Fall', 'Winter', 'Spring'), ('In-Class' 'Online'))
    ('Foundations of Computer Security', 'CSC557', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Software Engineering for Financial Markets', 'CSC559', ?,?,?,?, ('Spring'), ('In-Class' 'Online'))
    ('Intelligent Information Retrieval', 'CSC575', ?,?,?,?, ('Winter'), ('In-Class' 'Online'))
    ('Computational Advertising', 'CSC576', ?,?,?,?, ('Winter'), ('In-Class' 'Online'))
    ('Recommended Systems', 'CSC577', ?,?,?,?, ('Winter'), ('In-Class' 'Online'))
    ('Neural Networks and Deep Learning', 'CSC578', ?,?,?,?, ('Fall'), ('In-Class' 'Online'))
    ('Design of Object-Oriented Languages', 'CSC580', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Artificial Intelligence II', 'CSC583', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Cognitive Science', 'CSC587', ?,?,?,?, ('Winter'), ('In-Class' 'Online'))
    ('Topics in Database', 'CSC589', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Topics in User Interfaces', 'CSC590', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Topics in Algorithms', 'CSC591', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Topics in Computer Vision and Pattern Recognition', 'CSC592', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Topics in Artifical Intelligence', 'CSC594', ?,?,?,?, ('Fall', 'Spring'), ('In-Class' 'Online'))
    ('Topics in Computer Science', 'CSC595', ?,?,?,?, ('Winter'), ('In-Class' 'Online'))
    ('Topics in Data Analysis', 'CSC598', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Independent Study', 'CSC599', ?,?,?,?, ('Fall', 'Winter', 'Spring'), ('In-Class'))
    ('Master Research Continuation', 'CSC601', ?,?,?,?, ('Spring'), ('Online'))
    ('Predictive Analytics Capstone', 'CSC672', ?,?,?,?, ('Winter', 'Spring'), ('In-Class' 'Online'))
    ('Research Seminar', 'CSC690', ?,?,?,?, ('N/A'), ('In-Class' 'Online'))
    ('Master Research', 'CSC695', ?,?,?,?, ('All'), ('In-Class'))
    ('Master Research', 'CSC696', ?,?,?,?, ('All'), ('In-Class'))
    ('Graduate Internship', 'CSC697', ?,?,?,?, ('All'), ('In-Class'))
    ('Master Thesis', 'CSC698', ?,?,?,?, ('Fall'), ('In-Class'))
    ('Research', 'CSC699', ?,?,?,?, ('Fall', 'Winter', 'Spring'), ('In-Class' 'Online'))
    ]

ECT_courses [ ]
GAM_courses [ ]
GPH_courses [ ]
HCI_courses [ ]
HIT_courses [ ]
IS_courses [ ]
IT_courses [ ]
PM_courses [ ]
SE_courses [ ]
TDC_courses [ ]

