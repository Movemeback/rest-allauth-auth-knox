import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params, Router} from '@angular/router';

import {FormBuilder} from "@angular/forms";
import {AuthService} from "../auth.service";
import {RestAuthService} from "../restauth.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
})
export class LoginComponent implements OnInit {
  loginForm;
  loginRestAuthForm;
  result;
  restAuthResult;
  constructor(
    private router: Router,
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private restAuthService: RestAuthService,
    private route: ActivatedRoute
  ) {

    this.loginForm = this.formBuilder.group({
      username: '',
      password: ''
    });

    this.loginRestAuthForm = this.formBuilder.group({
      username: '',
      password: ''
    });

    // route.queryParams.subscribe((params: Params) => {
    //
    //         const parameter = params['code'];
    //
    //         if (!parameter && this.code) {
    //
    //             const queryParams = {};
    //             queryParams['code'] = this.code;
    //             queryParams['state'] = this.state;
    //
    //             this.router.navigate([], {
    //                 queryParams: queryParams,
    //                 queryParamsHandling: 'merge'
    //             });
    //         }
    //
    //     });

  }

  ngOnInit() {
    if (this.restAuthService.isSaved()) {
      this.restAuthService.socialLogin().subscribe( (response) => {
          this.restAuthResult = response;
          console.log(response);
          this.restAuthService.token = response['token'];
          this.restAuthService.clear();
          this.router.navigate(['/'])
        },
        (data) => {
          this.restAuthService.clear();
        });
    }
    this.route.queryParams.subscribe(params => {
      let code = params["code"];
      if (code) {
        let state = params["state"];
        this.restAuthService.save(code, state);

      }
    });



    // let code = this.route.snapshot.queryParams["code"];
    // if (code) {
    //   let state = this.route.snapshot.queryParams["state"];
    //   this.restAuthService.socialLogin(code, state).subscribe( (response) => {
    //     this.restAuthResult = response;
    //     console.log(response);
    //     this.restAuthService.token = response['token'];
    //     // this.router.navigate(['/'])
    //   } );
    //
    //
    // }

  }

  onSubmit(data) {
    console.log(data);
    this.authService.login(data['username'], data['password']).subscribe( (response) => {
      this.result = response; this.router.navigate(['/'])} );
  }

  onSubmitRestAuth(data) {
    console.log(data);
    this.restAuthService.login(data['username'], data['password']).subscribe( (response) => {
      this.restAuthResult = response;
      this.restAuthService.token = response['token'];
      this.router.navigate(['/'])
    } );
  }

}
