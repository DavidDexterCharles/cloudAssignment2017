import { Component, OnInit } from '@angular/core';

export class Transaction {
  id: string;name: string;bank:string;balance:string;
}


const TRANSACTION: Transaction[] = [
  { id:'U1001', name: 'Mr. Nice',bank:'Republic Bank',balance:'1000'},
  { id:'U2001', name: 'David Charles',bank:'Scotia Bank',balance:'1200'},
  { id:'U3001', name: 'Lion King',bank:'First citizens Bank',balance:'2534'}
];




@Component({
  selector: 'app-customer-details',
  templateUrl: './customer-details.component.html',
  styleUrls: ['./customer-details.component.css']
})
export class CustomerDetailsComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
