import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { AlertService } from '../_services/alert.service';
import { UserService } from '../_services/user.service';

@Component({
    moduleId: module.id,
    templateUrl: 'register.component.html',
    styleUrls: ['register.component.scss']
})

// TODO: Check if DePaul ID is already in the database.
export class RegisterComponent {
    model: any = {};
    loading = false;
    status: string;
    statuses = [
        'Active',
        'Graduated',
        'Frozen',
    ];
    genderType: string;
    genderTypes = [
        'Male',
        'Female',
        'Other',
        'Rather not say',
    ];
    personType: string;
    personTypes = [
        'Student',
        'Advisor',
    ];

    constructor(private router: Router,
                private userService: UserService,
                private alertService: AlertService) {
    }

    onPersonChange(personType: string) {
        this.personType = personType;
    }

    onGenderChange(genderType: string) {
        return genderType;
    }

    register() {
        this.loading = true;
        this.userService.create(this.model)
            .subscribe(
                data => {
                    this.alertService.success('Registration successful', true);
                    this.router.navigate(['/login']);
                },
                error => {
                    this.alertService.error(error);
                    this.loading = false;
                });
    }
}
