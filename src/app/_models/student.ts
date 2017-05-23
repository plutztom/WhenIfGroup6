import {User} from './user';
/**
 * Created by Cory Ginsberg on 5/4/2017.
 *
 * Student information
 *
 */

export class Student extends User {
    // TODO: remove 'id' and simply use DePaulID as the ID.
    id:              number;
    fullName:        string;
    depaulID:        number;
    status:          string; // Active, Graduated, or Frozen
    termStart:       Date;
    termEnd?:        Date;
    dateofBirth?:    Date;
    email:           string;
    phone?:          number;
    address?:        string;
    username:        string;
    password:        string;
}
