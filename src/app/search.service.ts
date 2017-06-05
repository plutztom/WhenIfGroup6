import { SearchComponent } from './search/search.component';
import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/distinctUntilChanged';
import 'rxjs/add/operator/switchMap';

@Injectable()
export class SearchService {

  baseUrl = 'https://api.cdnjs.com/libraries'; // TODO: Change this with actual url when backend is done.
  queryUrl = '?search='; // TODO: and the search as well.
  loading = false;

  constructor(private http: Http) {}

  search(terms: Observable<string>) {
      return terms.debounceTime(500)
                  .distinctUntilChanged()
                  .switchMap(term => this.searchEntries(term));
  }

  searchEntries(term) {
      this.loading = true;

      return this.http.get(this.baseUrl + this.queryUrl + term)
                      .map(res => res.json())
  }
}
