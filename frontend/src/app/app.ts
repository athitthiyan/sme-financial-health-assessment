import { Component, signal } from '@angular/core';
import { upload } from "./upload/upload";

@Component({
  selector: 'app-root',
  imports: [upload],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('frontend');
}
