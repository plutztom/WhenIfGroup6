/**
 * Created by coryg on 4/22/2017.
 */
import {Routes, RouterModule} from '@angular/router';

import {HomeComponent} from './home/home.component';
import {LoginComponent} from './login/login.component';
import {RegisterComponent} from './register/register.component';
import {AccountComponent} from './account/account.component';
import {AuthGuard} from './_guards/auth.guard';

const appRoutes: Routes = [
    {path: '', component: HomeComponent, canActivate: [AuthGuard]},
    {path: 'login', component: LoginComponent},
    {path: 'register', component: RegisterComponent},
    {path: 'account', component: AccountComponent},

    // otherwise redirect to home
    // {path: '**', redirectTo: ''}
];

export const routing = RouterModule.forRoot(appRoutes);
