import { EventEmitter } from '@angular/core';
import { Component, Input, Output } from '@angular/core';

@Component({
  selector: 'app-name',
  template: `
    <input type="text" [ngModel]="name" (ngModelChange)="onNameChange($event)">
    <p> Hey, my name is {{ name }} </p>
  `,
})
export class NameComponent {
  @Input() name!: string;
  @Output() nameChange = new EventEmitter();

  onNameChange(newName: string) {
    console.log('NameComponent: incoming new name', newName);
    this.name = newName;
    this.nameChange.emit(newName);
  }
}
