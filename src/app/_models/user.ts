export interface User {

    // TODO: remove 'id' and simply use DePaulID as the ID.
    // TODO: Update User, Student, and Faculty so that each is called properly as per the actual backend (See Data.sql).
    id:              number;
    fullName:        string;
    depaulID:        number;
    isAdvisor?:      boolean;

    username:        string;
    password:        string;

    jobTitle?:        string;

    status?:          string; // Active, Graduated, or Frozen
    termStart?:       Date;
    termEnd?:        Date;
    dateOfBirth?:    Date;
    email?:           string;
    phone?:          number;
    address?:        string;
    address2?:       string;
    city?:           string;
    state?:          string;
    zip?:            number;
}

export class Faculty implements User {
    // TODO: remove 'id' and simply use DePaulID as the ID.
    id:              number;
    fullName:        string;
    depaulID:        number;
    isAdvisor?:      boolean;

    username:        string;
    password:        string;

    jobTitle:        string;

    status?:          string; // Active, Graduated, or Frozen
    termStart?:       Date;
    termEnd?:        Date;
    dateOfBirth?:    Date;
    email:           string;
    phone?:          number;
    address?:        string;
    address2?:       string;
    city?:           string;
    state?:          string;
    zip?:            number;

}


export class Student implements User {
    id:              number;
    fullName:        string;
    depaulID:        number;
    isAdvisor?:      boolean;

    username:        string;
    password:        string;

    jobTitle?:        string;

    status:          string; // Active, Graduated, or Frozen
    termStart:       Date;
    termEnd?:        Date;
    dateOfBirth?:    Date;
    email:           string;
    phone?:          number;
    address?:        string;
    address2?:       string;
    city?:           string;
    state?:          string;
    zip?:            number;
}
