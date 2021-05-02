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
  public items: Observable<any[]>;

  constructor(private firestore: AngularFirestore) {
    // firestore.collection('teams').valueChanges().subscribe((data)=>{
    //   console.log('new')
    //   console.log(data);
    //   this.items = data;

    //   this.items.sort(function(a: any, b: any) {
    //     return a.points - b.points;
    //   });
    // },(err)=>{console.log(err)},()=>{
    //   console.log('finished')
    // })

    this.items =  firestore.collection('teams').valueChanges();

  //   .map((data) => {
  //     data.sort((a, b) => {
  //         return a < b ? -1 : 1;
  //      });
  //     return data;
  //  });
    
    console.log(firestore.collection('teams').valueChanges())

  }

  ngOnInit(){

  }

}
