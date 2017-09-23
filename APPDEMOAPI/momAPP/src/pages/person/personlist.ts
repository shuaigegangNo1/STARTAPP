/**
 * Created by huangxuewen on 2017/9/20.
 */
import {Component} from "@angular/core";
import {AlertController, NavController} from "ionic-angular";
import {PersonService} from "../../common/service/personService";
import {PersonComponent} from "./person"
@Component({
  selector: 'app-person-list',
  templateUrl: 'personlist.html'
})
export class PersonList {

  TaskName: string = "MyTasks";

  personList: any[];
  myTasks: any[];

  constructor(protected navCtrl: NavController, protected alertCtrl: AlertController,
              private personService: PersonService) {
    this.initGetTaskList();
  }

  // ngOnInit() {
  //   super.ngOnInit();
  //   this.initGetTaskList();
  // }

  goToTaskDetail(person) {
    const item = {
      id: person[0],
    };
    this.navCtrl.push(PersonComponent, {
      person: item
    });
  }

  initGetTaskList() {
    // this.totalTasks = this.taskService.getTaskList();
    this.personService.getPersonList().subscribe(res =>{
      console.log(">>>>data>>>>", this.personList = res.result)
      this.personList = res.result}
    );
  }

  searchTasks(ev: any) {
    this.initGetTaskList();
    //TODO: search logically in backend
    // set val to the value of the searchbar
    let val = ev.target.value;
    // if the value is an empty string don't filter the items
    // if (val && val.trim() != '') {
    //   this.totalTasks = this.totalTasks.filter((item) => {
    //     return (item.name.indexOf(val) !== -1);
    //   })
    //   this.myTasks = this.totalTasks.filter((item) => {
    //     return (item.name.indexOf(val) !== -1);
    //   })
    // }
  }
}
