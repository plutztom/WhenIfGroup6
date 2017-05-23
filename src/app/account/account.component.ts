import {Component, OnInit} from '@angular/core';
import {User, Student, Faculty} from '../_models/user';
import {UserService} from '../_services/user.service';
import {Router} from '@angular/router';
import {AlertService} from '../_services/alert.service';
import { Click } from '../click';
import { MdDialogRef, MdDialog } from '@angular/material';

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
    statuses = [
        'Active',
        'Graduated',
        'Frozen',
    ];

    constructor(private userService: UserService,
                private router: Router,
                private alertService: AlertService,
                public dialog: MdDialog) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
    }

    openDialog() {
        const dialogRef = this.dialog.open(DeleteDialogComponent);
        dialogRef.afterClosed().subscribe(result => {
            this.delete = result;
        });
    }

    deleteUser(id: number) {
        this.userService.delete(id)
            .subscribe(
                data => {
                    this.alertService.success('Your account has been deleted.', true);
                    this.router.navigate(['/login']);
                },
                error => {
                    this.alertService.error(error);
                }
            );
    }

    ngOnInit() {
    }

    update() {
        this.userService.update(this.currentUser)
            .subscribe(
                data => {
                    this.alertService.success('Your account has been updated.', true);
                    this.router.navigate(['/']);
                },
                error => {
                    this.alertService.error(error);
                });
    }

    checkUser(currentUser) {
        return typeof currentUser;
    }
}

Component({
    selector: 'when-if-delete-dialog',
    templateUrl: './when-if-delete-dialog.html'
})
export class DeleteDialogComponent {
    constructor(public dialogRef: MdDialogRef<DeleteDialogComponent>) {}
}
