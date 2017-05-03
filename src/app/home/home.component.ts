import {Component, OnInit} from '@angular/core';

import {User} from '../_models/user';
import {UserService} from '../_services/user.service';
import { Ng2SmartTableModule, LocalDataSource } from 'ng2-smart-table';

@Component({
    moduleId: module.id,
    templateUrl: 'home.component.html'
})

export class HomeComponent implements OnInit {
    currentUser: User;
    users: User[] = [];
    isAdvisor: boolean;
    source: LocalDataSource;

    settings = {
        columns: {
            fullName: {
                title: 'Name',
            },
            username: {
                title: 'Username',
            },
            depaulID: {
                title: 'ID Number',
                editable: false,
                addable: false,
            },
            email: {
                title: 'Email',
            },
        },
    };

    constructor(private userService: UserService) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
        this.isAdvisor = JSON.parse(localStorage.getItem('currentUser.isAdvisor'));

        this.source = new LocalDataSource();

        this.userService.getAll().subscribe(data => {
            this.source.load(data);
        })
    }

    ngOnInit() {
        this.loadAllUsers();
    }

    showAdvisor() {
        return this.isAdvisor;
    }

    private showAll() {
        this.userService.getAll();
    }

    private loadAllUsers() {
        this.userService.getAll().subscribe(users => {
            this.users = users;
        });
    }
}
