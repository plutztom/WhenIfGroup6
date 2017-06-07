import { Component, OnInit } from '@angular/core';
import { User, Student, Faculty } from '../_models/user';
import { UserService } from '../_services/user.service';
import { Router } from '@angular/router';
import { AlertService } from '../_services/alert.service';
import { MdSnackBar } from '@angular/material';

interface UserInfo {
    id: number;
    fullName: string;
    depaulID: number;
    isAdvisor?: boolean;

    username: string;
    password: string;

    jobTitle?: string;

    status?: string; // Active, Graduated, or Frozen
    termStart?: Date;
    termEnd?: Date;
    dateOfBirth?: Date;
    email?: string;
    phone?: number;
}

@Component({
    selector: 'when-if-account',
    templateUrl: './account.component.html',
    styleUrls: ['./account.component.scss']
})
export class AccountComponent implements OnInit {
    currentUser: any = {};
    delete?= false;
    status: string;
    userInfo: UserInfo;
    statuses = [
        'Active',
        'Graduated',
        'Frozen',
    ];
    majors = [
        'MS Computer Science',
        'MS Information Systems',
    ];

    constructor(private userService: UserService,
        private router: Router,
        private alertService: AlertService,
        public snackBar: MdSnackBar) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
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
