import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import {QuestionService} from "../question.service";
import {FormBuilder} from "@angular/forms";
import {AuthService} from "../auth.service";
import {RestAuthService} from "../restauth.service";

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
})
export class RegistrationComponent implements OnInit {
  registrationForm;
  registrationRestAuthForm;
  result;
  resultRestAuth;
  constructor(
    private router: Router,
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private restAuthService: RestAuthService
  ) {

    this.registrationForm = this.formBuilder.group({
      first_name: '',
      last_name: '',
      username: '',
      password: ''
    });

    this.registrationRestAuthForm = this.formBuilder.group({
      first_name: '',
      last_name: '',
      username: '',
      email: '',
      password1: '',
      password2: ''
    });

  }

  ngOnInit() {
  }

  onSubmit(data) {
    this.authService.register(data['first_name'], data['last_name'], data['username'], data['password']).subscribe( (response) => {
      this.result = response; this.router.navigate(['/']);
    })
  }

  onSubmitRestAuth(data) {
    this.restAuthService.register(data['first_name'], data['last_name'], data['username'], data['email'], data['password1'], data['password2']).subscribe( (response) => {
      this.resultRestAuth = response;
      this.restAuthService.token = response['token'];
      this.router.navigate(['/']);
    })
  }

}
