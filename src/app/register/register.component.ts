import { Faculty, Student } from './../_models/user';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MdSnackBar, MdTabsModule } from '@angular/material';

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
    currentTab = 0;
    selectedIndex = 0;
    statuses = [
        'Active',
        'Graduated',
        'Frozen',
    ];
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
                private alertService: AlertService,
                public snackBar: MdSnackBar) {
    }

    onGenderChange(genderType: string) {
        return genderType;
    }

    register() {
        // Set Advisor status based on Current Tab
        // if (this.currentTab === 0) { this.model.isAdvisor = false; } else { this.model.isAdvisor = true; }

        this.userService.create(this.model)
            .subscribe(
                data => {
                    this.router.navigate(['/']);
                    this.snackBar.open('Registration Successful', 'Dismiss', {
                        duration: 2000,
                    });
                },
                error => {
                    this.snackBar.open('Error: ' + error, 'Dismiss', {
                        duration: 2000,
                    });
                });
    }

}
