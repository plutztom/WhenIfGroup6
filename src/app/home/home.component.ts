import { MdSnackBar } from '@angular/material';
import { Jsonp, ConnectionBackend } from '@angular/http';
import { SearchService } from './../search.service';
import { Component, OnInit, ViewChild, Input } from '@angular/core';

import { User } from '../_models/user';
import { Class } from '../_models/class';
import { Choice } from './../_models/choice';

import { UserService } from '../_services/user.service';
import { Router, ActivatedRoute } from '@angular/router';
import { AlertService } from '../_services/alert.service';
import { AuthenticationService } from '../_services/authentication.service';

@Component({
    moduleId: module.id,
    templateUrl: 'home.component.html',
    styleUrls: ['home.component.scss'],
    providers: [SearchService, Jsonp]
})

export class HomeComponent implements OnInit {
    @Input() search: string;

    choice: Choice;
    searchQuery: string;
    returnUrl: string;
    currentUser: User;

    selectedMajor: string;

    users: User[] = [];

    classesArray: Array<string> = ['1', '2', '3'];
    quarters = [
        'Fall 2018',
        'Winter 2018',
        'Spring 2018',
        'Fall 2019',
        'Winter 2019',
        'Spring 2019',
    ];
    classTypes = [
        'In Class',
        'Online',
        'Either',
    ];
    numbers = [
        'One',
        'Two',
        'Three',
        'Four',
    ];
    csConcentrations = [
        'General',
    ];
    isConcentrations = [
        'Standard',
        'IT Enterprise Management',
        'Database Administration',
        'Business Intelligence',
        'Business Analysis/System Analysis',
    ];

    constructor(private userService: UserService,
        private route: ActivatedRoute,
        private authenticationService: AuthenticationService,
        private router: Router,
        private alertService: AlertService,
        private searchService: SearchService,
        public snackBar: MdSnackBar) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
    }

    onKey(term) {
        this.searchService.search(term);
    }

    ngOnInit() {
        this.loadAllUsers();

        this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
    }

    // TODO: Implement WhenIf calculations once the backend is completed.
    whenIf() {
        alert('Sorry! Not ready yet!');
    }

    onMajorChange($event) {
        this.selectedMajor = $event.target.value;
    }

    showAdvisor() {
        return this.currentUser.isAdvisor;
    }

    private loadAllUsers() {
        this.userService.getAll().subscribe(users => {
            this.users = users;
        });
    }

    login(username, password) {
        this.authenticationService.login(username, password)
            .subscribe(
            data => {
                this.router.navigate([this.returnUrl]);
            },
            error => {
                this.snackBar.open('Error: ' + error, 'Dismiss', {
                    duration: 2000,
                });
            });
    }
}
