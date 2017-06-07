import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';

import { Student } from '../_models/user';
import { Faculty } from '../_models/user';

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

    create(user: any) {
        return this.http.post('/api/users', user, UserService.jwt()).map((response: Response) => response.json());
    }

    update(user: any) {
        return this.http.post('/api/users/' + user, UserService.jwt()).map((response: Response) => response.json());
    }

    // Design sheet calls for people to be able to delete themselves.
    delete(id: number) {
        return this.http.delete('/api/users/' + id, UserService.jwt()).map((response: Response) => response.json());
    }

    // private helper methods
    private static jwt() {
        // create authorization header with jwt token
        const currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.token) {
            const headers = new Headers({ 'Authorization': 'Bearer ' + currentUser.token });
            return new RequestOptions({ headers: headers });
        }
    }
}
