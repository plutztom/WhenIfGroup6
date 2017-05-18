import { Component, OnInit } from '@angular/core';

import { User } from '../_models/user';
import { Class } from '../_models/class'
import { When } from '../_models/when'
import { UserService } from '../_services/user.service';
import { Ng2SmartTableModule, LocalDataSource } from 'ng2-smart-table';

@Component({
    moduleId: module.id,
    templateUrl: 'home.component.html',
    styleUrls: ['home.component.scss']
})

export class HomeComponent implements OnInit {
    currentUser: User;
    users: User[] = [];
    isAdvisor: boolean;
    source: LocalDataSource;
    working = false;
    whenParams: When;
    classesArray:Array<string> = ['1', '2', '3'];

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

    // TODO: Implement WhenIf calculations once the backend is completed.
    whenIf() {

    }

    showAdvisor() {
        return this.currentUser.isAdvisor;
    }

    setWorking() {
        this.working = true;
    }

    isWorking() {
        return this.working;
    }

    private loadAllUsers() {
        this.userService.getAll().subscribe(users => {
            this.users = users;
        });
    }
}
