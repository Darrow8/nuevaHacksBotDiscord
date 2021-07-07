import { Component, OnInit } from '@angular/core';
import { AngularFirestore } from '@angular/fire/firestore';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'nuevahacks-leaderboard';
  public teams: Observable<any[]>;
  public tasks: Observable<any[]>;

  constructor(private firestore: AngularFirestore) {


    this.teams =  firestore.collection('teams').valueChanges();
    this.tasks = firestore.collection('tasks').valueChanges();




  }

  ngOnInit(){

  }

}
