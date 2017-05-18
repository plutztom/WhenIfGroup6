export class User {

    // TODO: remove 'id' and simply use DePaulID as the ID.
    // TODO: Update User, Student, and Faculty so that each is called properly as per the actual backend (See Data.sql).
    id:              number;
    fullName:        string;
    depaulID:        number;
    isAdvisor?:      boolean;

    dateofBirth:     Date;
    email:           string;
    phone?:          number;
    address?:        string;

    username:        string;
    password:        string;
    confirmPassword: string;
}
