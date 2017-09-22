/**
 * Created by huangxuewen on 2017/9/20.
 */
import {Component} from "@angular/core";
import {AlertController, NavController, NavParams} from "ionic-angular";
import {PersonService} from "../../common/service/personService";
import {person} from "../../common/model/person"
import {PersonList} from "./personlist";
@Component({
  selector: 'app-person',
  templateUrl: 'person.html'
})
export class PersonComponent{
  id: string;
  firstname: string;
  lastname: string;
  telephone: string;
  address: string;
  city: string;
  person =new person();
  personId: string;
  personInfo: any = [];
  buttonName: string = '添加';
  constructor(public navCtrl: NavController, public alertCtrl: AlertController,
              private personService: PersonService, private navParams:NavParams){
    if(this.navParams.get('person')) {
      this.personId = this.navParams.get('person').id;
      this.getPersonDetail();
      this.buttonName = '修改';
    }

  }
  addPerson() {
    this.person.id = this.id;
    this.person.firstname = this.firstname;
    this.person.lastname = this.lastname;
    this.person.telephone = this.telephone;
    this.person.city = this.city;
    this.person.address= this.address;
    this.person.create_date = '2017-09-26';
    this.personService.createPerson(this.person).subscribe(res => {
        console.log(">>>>data>>>",res);
        this.navCtrl.push(PersonList);
      }
    )
    // let NewPerson = {
    //   id: this.id,
    //
    // }
  }
  getPersonDetail() {
    this.personService.getPersonDetail(this.personId).subscribe(res =>
    {
      this.personInfo = res.person;
      this.id = this.personInfo[0][0];
      this.lastname = this.personInfo[0][1];
      this.firstname = this.personInfo[0][2];
      this.city = this.personInfo[0][3];
      this.address = this.personInfo[0][4];
      this.telephone = this.personInfo[0][6];
      console.log(">>>>res",this.personInfo[0][1])

    })
  }
}
