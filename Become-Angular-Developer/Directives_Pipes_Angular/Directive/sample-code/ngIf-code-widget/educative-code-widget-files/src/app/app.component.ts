import { Component, OnInit } from '@angular/core';

interface User {
  name: string;
  premium: boolean;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  userA: User | undefined;
  userB: User | undefined;
  userC: User | undefined;
  userD: User | undefined;

  ngOnInit() {
    setTimeout(() => {

      this.userA = { name: 'John Doe', premium: false };
      this.userB = { name: 'Jane Doe', premium: true };
      this.userC = undefined;
      this.userD = { name: '', premium: true };

    }, 10000)
  }
}
