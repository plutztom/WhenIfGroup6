import {Component, OnInit} from '@angular/core';
import {User} from '../_models/user';
import {UserService} from '../_services/user.service';
import {Router} from '@angular/router';
import {AlertService} from '../_services/alert.service';

@Component({
    selector: 'app-account',
    templateUrl: './account.component.html',
    styleUrls: ['./account.component.scss']
})
export class AccountComponent implements OnInit {
    currentUser: User;
    loading = false;

    constructor(private userService: UserService,
                private router: Router,
                private alertService: AlertService) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
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
        this.loading = true;
        this.userService.update(this.currentUser)
            .subscribe(
                data => {
                    this.alertService.success('Your account has been updated.', true);
                    this.router.navigate(['/']);
                },
                error => {
                    this.alertService.error(error);
                    this.loading = false;
                });
    }

}
