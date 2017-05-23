export interface User {

    // TODO: remove 'id' and simply use DePaulID as the ID.
    // TODO: Update User, Student, and Faculty so that each is called properly as per the actual backend (See Data.sql).
    id:              number;
    fullName:        string;
    depaulID:        number;
    isAdvisor?:      boolean;
    // jobTitle:        string;

    username:        string;
    password:        string;
}

export interface Faculty extends User {
    // TODO: remove 'id' and simply use DePaulID as the ID.
    jobTitle:        string;

}


export interface Student extends User {
    // TODO: remove 'id' and simply use DePaulID as the ID.

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
