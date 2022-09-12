<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
        <Modal id="modal-demo" ref="modal" v-model="showModal" :header="false" size="lg" @hide="restartApp">
            <Alert type="success" v-html="modalText">
            </Alert>
        </Modal>
        <ProgressBar v-model="progress" label />
        <div v-show="showStepOne">
            <h3>The first step is to register a business</h3>
            <div class="form-group">
                <label for="inputName">Business Name</label>
                <input v-model="businessName" type="text" id="inputName" class="form-control input-lg" placeholder="Enter business name">
                <small id="emailHelp" class="form-text text-muted">We'll never share your details with anyone else.</small>
            </div>
            <div class="form-group">
                <label for="inputAmount">Loan Amount in Australian Dollars</label>
                <input v-model="loanAmount" type="number" id="inputAmount" class="form-control input-lg" placeholder="e.g. 5000">
            </div>
            <Btn size="lg" type="success" @click=registerBusiness>Register Business</Btn>
        </div>
        <div v-show="showStepTwo">
            <h3>
                We have registered your business {{ businessName }} for the loan amount of {{ loanAmount }}.<br>
                The second step is to select an accounting provider below and request a Balance Sheet.
            </h3>
            <div v-for="accountingProvider in accountingProviders" :key="accountingProvider.id">
                <h3>{{ accountingProvider.name }}</h3>
                <img :src="accountingProvider.logo" height="200"><br>
                <Btn size="lg" type="success" @click=requestBalanceSheet(accountingProvider.id)>
                    Request Balance Sheet from {{ accountingProvider.name }}
                </Btn>
                <hr>
            </div>
        </div>
        <div v-show="showStepThree">
            <h3>
                We have retrieved the Balance Sheet below.<br>
                The third step is to send this Balance Sheet to a Decision Engine.
                Please click the button below to proceed.
            </h3>
            <table class="table">
                <thead>
                <tr>
                    <th scope="col">Year</th>
                    <th scope="col">Month</th>
                    <th scope="col">Assets Value</th>
                    <th scope="col">Profits</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(entry, key) in balanceSheet" :key="key">
                    <td>{{ entry.year }}</td>
                    <td>{{ entry.month }}</td>
                    <td>{{ entry.assetsValue }}</td>
                    <td>{{ entry.profitOrLoss }}</td>
                </tr>
                </tbody>
            </table>
            <Btn size="lg" type="success" @click=sendToDecisionEngine()>
                Send Balance Sheet to Decision Engine
            </Btn>
        </div>
    </div>
</template>

<script>
import { Modal, Btn, ProgressBar, Alert } from 'uiv'
const axios = require('axios');
export default {
    name: 'BusinessLoanApp',
    props: {
        msg: String
    },
    components: {
        Modal,
        Btn,
        ProgressBar,
        Alert
    },
    methods: {
        registerBusiness: function () {
            axios.post(
                'http://localhost:8000/business/',
                { name: this.businessName, loan_amount: this.loanAmount },
            ).then(() => {
                this.progress = 33
                // this.showModal = true
                // this.modalText = `Well done! We have registered your business ${this.businessName}, and started your
                // loan application for AUD$ ${this.loanAmount}.`
                this.showStepOne = false
                this.showStepTwo = true
                axios.get(
                    'http://localhost:8000/accounting-provider/'
                ).then((resp) => {
                    this.accountingProviders = resp.data
                })
            }).catch((e) => {
                this.showModal = true
                this.modalText = `Unfortunately and error occurred: ${e}`
            })
        },
        requestBalanceSheet: function (accountingProviderPrimaryKey) {
            axios.get(
                `http://localhost:8000/request-balance-sheet-from-accounting-provider/${accountingProviderPrimaryKey}`
            ).then((resp) => {
                axios.get(
                    resp.data.url
                ).then((resp) => {
                    this.showStepTwo = false
                    this.showStepThree = true
                    this.balanceSheet = resp.data
                    this.progress = 66
                }).catch((e) => {
                    this.showModal = true
                    this.modalText = `Unfortunately and error occurred: ${e}`
                })
            })
        },
        sendToDecisionEngine: function () {
            axios.post(
                'http://127.0.0.1:8003/process-balance-sheet',
                {
                    balanceSheet: this.balanceSheet,
                    businessName: this.businessName,
                    loanAmount: this.loanAmount
                },
            ).then((resp) => {
                this.modalText = `<h1>Congratulations! your assessment has been processed with the results below:<br>
                Business name: ${resp.data.business_name}<br>
                Year established: ${resp.data.year_established}<br>
                Pre-Assessment: ${resp.data.preAssessment}</h1>`
                this.progress = 100
                this.showModal = true
            }).catch((e) => {
                this.showModal = true
                this.modalText = `Unfortunately and error occurred: ${e}`
            })
        },
        restartApp: function () {
            if (this.showStepThree === true) {
                this.progress = 0
                this.showStepThree = false
                this.showStepOne = true
                this.businessName = ""
                this.loanAmount = 0
                this.showModal = false
                this.modalText = ""
                this.accountingProviders = []
                this.balanceSheet = []
                this.preAssessment = 20
                this.yearEstablished = 2022
            }
        }
    },
    data: () => ({
        progress: 0,
        businessName: "",
        loanAmount: 0,
        showModal: false,
        modalText: "",
        showStepOne: true,
        showStepTwo: false,
        showStepThree: false,
        accountingProviders: [],
        balanceSheet: [],
        preAssessment: 20,
        yearEstablished: 2022
    })
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
</style>
