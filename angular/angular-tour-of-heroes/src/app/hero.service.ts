import { Injectable } from "@angular/core";

// reactive extensions library for javascript
import { Observable, of } from "rxjs";

import { Hero } from "./hero";
import { HEROES } from "./mock-heroes";
import { MessageService } from "./message.service";

@Injectable({
  providedIn: "root",
})
export class HeroService {
  constructor(private messageService: MessageService) {}

  getHeroes(): Observable<Hero[]> {
    // TODO: send the message _after_ fetching the heroes
    this.messageService.add("HeroService: fetched heroes");
    // pretends that the "HEROES" is the database we're calling from for now
    return of(HEROES);
  }
}
