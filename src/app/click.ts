import {AuthenticationService} from './_services/authentication.service';

export class Click {
    constructor(
                private authenticationService: AuthenticationService) {
    }

    onLogout() {
        this.authenticationService.logout();

    }
}
