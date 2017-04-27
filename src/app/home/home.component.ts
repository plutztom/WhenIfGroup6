import {Component, OnInit} from '@angular/core';

import {User} from '../_models/user';
import {UserService} from '../_services/user.service';

@Component({
    moduleId: module.id,
    templateUrl: 'home.component.html'
})

export class HomeComponent implements OnInit {
    currentUser: User;
    users: User[] = [];
    isAdmin: boolean;

    constructor(private userService: UserService) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
        this.isAdmin = JSON.parse(localStorage.getItem(''));
    }

    ngOnInit() {
        this.loadAllUsers();
    }

    showAdmin() {
        return this.isAdmin;
    }

    private loadAllUsers() {
        this.userService.getAll().subscribe(users => {
            this.users = users;
        });
    }
}
