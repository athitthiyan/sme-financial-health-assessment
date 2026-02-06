import { Component } from '@angular/core';
import { NgIf } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [NgIf, HttpClientModule],
  templateUrl: './upload.html'
})
export class upload {
  file!: File;
  result: any;

  constructor(private http: HttpClient) {}

  onFileChange(event: any) {
    this.file = event.target.files[0];
  }

  upload() {
    const formData = new FormData();
    formData.append('file', this.file);

    this.http
      .post('http://127.0.0.1:8000/analyze', formData)
      .subscribe(res => (this.result = res));
  }
}
