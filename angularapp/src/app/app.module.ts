import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {ReactiveFormsModule} from "@angular/forms";
import {RouterModule} from "@angular/router";
import {QuestionListComponent} from "./question-list/question-list.component";
import {QuestionDetailsComponent} from "./question-details/question-details.component";
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {QuestionService} from "./question.service";
import { UserComponent } from './user/user.component';
import {UserService} from "./user.service";
import {AuthService} from "./auth.service";
import {LoginComponent} from "./login/login.component";
import {RegistrationComponent} from "./registration/registration.component";
import {RestAuthService} from "./restauth.service";
import {AuthenticationInterceptor} from "./authentication.interceptor";


@NgModule({
  declarations: [
    AppComponent,
    QuestionListComponent,
    QuestionDetailsComponent,
    UserComponent,
    LoginComponent,
    RegistrationComponent
  ],

  imports: [
    HttpClientModule,
    BrowserModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: '', component: QuestionListComponent },
      { path: 'questions/:questionId', component: QuestionDetailsComponent },
      { path: 'profile', component: UserComponent },
      { path: 'login', component: LoginComponent },
      { path: 'registration', component: RegistrationComponent },
    ])
  ],
  providers: [AuthService, RestAuthService, QuestionService, UserService, {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthenticationInterceptor,
      multi: true
    } ],
  bootstrap: [AppComponent]
})
export class AppModule { }
