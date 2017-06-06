import { SearchService } from './../search.service';
import { Component } from '@angular/core';
import { Subject } from 'rxjs/Subject';
import { FormControl } from '@angular/forms';

import 'rxjs/add/operator/startWith';
import 'rxjs/add/operator/map';

@Component({
  selector: 'when-if-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss'],
  providers: [SearchService]
})
export class SearchComponent {
  searchCtrl: FormControl;
  results: Object;
  searchTerm$ = new Subject<string>();

  constructor(public searchService: SearchService) {
      this.searchCtrl = new FormControl();
      this.searchService.search(this.searchTerm$)
          .subscribe(results => {
              this.results = results.results;
              this.searchService.loading = false;
          });
   }
}
