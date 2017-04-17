import {Injectable} from '@angular/core';
import {Http, Headers, RequestOptions, Response} from '@angular/http';

import {User} from '../_models/user';

@Injectable()
export class UserService {
    constructor(private http: Http) {
    }

    getAll() {
        return this.http.get('/api/users', UserService.jwt()).map((response: Response) => response.json());
    }

    getById(id: number) {
        return this.http.get('/api/users/' + id, UserService.jwt()).map((response: Response) => response.json());
    }

    create(user: User) {
        return this.http.post('/api/users', user, UserService.jwt()).map((response: Response) => response.json());
    }

    update(user: User) {
        return this.http.put('/api/users/' + user.id, user, UserService.jwt()).map((response: Response) => response.json());
    }

    // No need to delete users since they will be added beforehand.
    //delete(id: number) {
    //    return this.http.delete('/api/users/' + id, this.jwt()).map((response: Response) => response.json());
    //}

    // private helper methods

    private static jwt() {
        // create authorization header with jwt token
        let currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.token) {
            let headers = new Headers({'Authorization': 'Bearer ' + currentUser.token});
            return new RequestOptions({headers: headers});
        }
    }
}
