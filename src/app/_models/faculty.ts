import {User} from './user';
/**
 * Created by Cory Ginsberg on 5/4/2017.
 *
 * Faculty information
 *
 */

export class Faculty extends User {
    // TODO: remove 'id' and simply use DePaulID as the ID.
    id:              number;
    fullName:        string;
    depaulID:        number;
    jobTitle:        string; // Active, Graduated, or Frozen

}
