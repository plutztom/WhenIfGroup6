import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {Location, LocationStrategy, PathLocationStrategy} from '@angular/common';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
    providers: [Location, {provide: LocationStrategy, useClass: PathLocationStrategy}]
})
export class NavbarComponent implements OnInit {
    constructor(public route:ActivatedRoute, public location: Location) { }

    ngOnInit() {

    }

}
