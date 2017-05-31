import { Component, OnInit, ViewChild } from '@angular/core';

import { User } from '../_models/user';
import { Class } from '../_models/class';
import { UserService } from '../_services/user.service';
import {Router, ActivatedRoute} from '@angular/router';
import {AlertService} from '../_services/alert.service';
import {AuthenticationService} from '../_services/authentication.service';
class WhenIfInput {
    quarter: string;
    year: string;
    working?: boolean;
    classesPer: number;
}

@Component({
    moduleId: module.id,
    templateUrl: 'home.component.html',
    styleUrls: ['home.component.scss']
})

export class HomeComponent implements OnInit {
    returnUrl: string;

    currentUser: User;
    search: string;
    quarterValue: string;
    yearValue: number;
    classesPerQuarter: number;
    input: WhenIfInput;
    users: User[] = [];
    isAdvisor: boolean;
    working = false;
    classesArray: Array<string> = ['1', '2', '3'];
    quarters = [
        'Fall',
        'Winter',
        'Spring',
    ];
    years = [
        '2017',
        '2018',
        '2019',
        '2020',
    ];
    numbers = [
        'One',
        'Two',
        'Three',
        'Four',
    ];

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

  rows = [];

  temp = [];

  columns = [
    { prop: 'Full Name' },
    { name: 'DePaul ID' },
    { name: 'Status' }
  ];

    constructor(private userService: UserService,
                private route: ActivatedRoute,
                private authenticationService: AuthenticationService,
                private router: Router,
                private alertService: AlertService) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
        this.isAdvisor = JSON.parse(localStorage.getItem('currentUser.isAdvisor'));

        this.rows = JSON.parse(localStorage.getItem('currentUser'));
    }

    ngOnInit() {
        this.loadAllUsers();

        this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';

    }

    onChange() {

    }

    // TODO: Implement WhenIf calculations once the backend is completed.
    whenIf() {
        alert('Sorry! Not ready yet!');
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

    updateFilter(event) {
    const val = event.target.value.toLowerCase();

    // filter our data
    const temp = this.temp.filter(function(d) {
      return d.name.toLowerCase().indexOf(val) !== -1 || !val;
    });

    // update the rows
    this.rows = temp;
    // Whenever the filter changes, always go back to the first page
  }

  login(username, password) {
        this.authenticationService.login(username, password)
            .subscribe(
                data => {
                    this.router.navigate([this.returnUrl]);
                },
                error => {
                    this.alertService.error(error);
                });
    }

}
