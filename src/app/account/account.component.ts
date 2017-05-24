import {Component, OnInit} from '@angular/core';
import {User, Student, Faculty} from '../_models/user';
import {UserService} from '../_services/user.service';
import {Router} from '@angular/router';
import {AlertService} from '../_services/alert.service';
import { Click } from '../click';
import { MdSnackBar } from '@angular/material';

interface UserInfo {
    id:              number;
    fullName:        string;
    depaulID:        number;
    isAdvisor?:      boolean;

    username:        string;
    password:        string;

    jobTitle?:       string;

    status?:         string; // Active, Graduated, or Frozen
    termStart?:      Date;
    termEnd?:        Date;
    dateOfBirth?:    Date;
    email?:          string;
    phone?:          number;
    address?:        string;
    address2?:       string;
    city?:           string;
    state?:          string;
    zip?:            number;
}

@Component({
    selector: 'when-if-account',
    templateUrl: './account.component.html',
    styleUrls: ['./account.component.scss']
})
export class AccountComponent implements OnInit {
    currentUser: Student | Faculty;
    click: Click;
    delete? = false;
    status: string;
    userInfo: UserInfo;
    statuses = [
        'Active',
        'Graduated',
        'Frozen',
    ];

    constructor(private userService: UserService,
                private router: Router,
                private alertService: AlertService,
                public snackBar: MdSnackBar) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));

            // Below sets all the parameters from students and faculty to the userInfo for use in the HTML of this component.


        if (this.currentUser instanceof Student) {
            this.currentUser.fullName = this.userInfo.fullName;
            this.currentUser.depaulID = this.userInfo.depaulID;
            this.currentUser.username = this.userInfo.username;
            this.currentUser.password = this.userInfo.password;

            this.currentUser.status = this.userInfo.status;
            this.currentUser.termStart = this.userInfo.termStart;
            this.currentUser.termEnd = this.userInfo.termEnd;
            this.currentUser.dateOfBirth = this.userInfo.dateOfBirth;
            this.currentUser.email = this.userInfo.email;
            this.currentUser.phone = this.userInfo.phone;
            this.currentUser.address = this.userInfo.address;
            this.currentUser.address2 = this.userInfo.address2
            this.currentUser.city = this.userInfo.city;
            this.currentUser.state = this.userInfo.state;
            this.currentUser.zip = this.userInfo.zip;

        } else if (this.currentUser instanceof Faculty) {
            this.currentUser.fullName = this.userInfo.fullName;
            this.currentUser.depaulID = this.userInfo.depaulID;
            this.currentUser.username = this.userInfo.username;
            this.currentUser.password = this.userInfo.password;

            this.currentUser.jobTitle = this.userInfo.jobTitle;
        }
    }

    deleteUser(id: number) {
        this.userService.delete(id)
            .subscribe(
                data => {
                    this.snackBar.open('Your account has been deleted.', 'Dismiss', {
                        duration: 2000,
                    });
                    this.router.navigate(['/login']);
                },
                error => {
                    this.snackBar.open('Error: ' + error, 'Dismiss', {
                        duration: 2000,
                    });
                }
            );
    }

    ngOnInit() {
    }

    update() {
        this.userService.update(this.currentUser)
            .subscribe(
                data => {
                    this.snackBar.open('Your account has been updated.', 'Dismiss', {
                        duration: 2000,
                    });
                    this.router.navigate(['/']);
                },
                error => {
                    this.snackBar.open('Error: ' + error, 'Dismiss', {
                        duration: 2000,
                    });
                }
            );
    }

    checkUser(currentUser) {
        return typeof currentUser;
    }
}
