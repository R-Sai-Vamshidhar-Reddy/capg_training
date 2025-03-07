import React, {useState} from 'react';

function InterestCalculator(){
    const [principal, setPrincipal]=useState('');
    const [rate, setRate]=useState('');
    const [time, setTime]=useState('');
    const [type, setType]=useState('');
    const [result, setResult]=useState(null);

    const calculateInterest=()=>{
        let P=parseFloat(principal);
        let R=parseFloat(rate);
        let T=parseFloat(time);

        if (isNaN(P) || isNaN(R) || isNaN(T) || P<=0 || R<=0 || T<=0){
            setResult("Please enter valid values.");
            return;
        }

        let interest=0;
        if(type==="simple"){
            interest=(P*T*R)/100;
        }
        else{
            interest=P*(Math.pow((1+R/100),T))-P;
        }
        setResult(`The calculated ${type} interest is: ${interest.toFixed(2)}`);   
    }
    return (
        <div style={styles.container}>
            <h2>Interest Calculator</h2>
            <label>Principal Amount (P): </label>
            <input 
                type="number" 
                value={principal} 
                onChange={(e) => setPrincipal(e.target.value)} 
                style={styles.input}
                placeholder="Enter Principal Amount"
            />

            <label>Rate of Interest (R): </label>
            <input 
                type="number" 
                value={rate} 
                onChange={(e) => setRate(e.target.value)} 
                style={styles.input}
                placeholder="Enter Rate Of interest"
            />

            <label>Time (T): </label>
            <input 
                type="number" 
                value={time} 
                onChange={(e) => setTime(e.target.value)}
                style={styles.input} 
                placeholder="Enter Time"
            />

            <label>Interest Type: </label>
            <select value={type} onChange={(e) => setType(e.target.value)}>
                <option value="simple">Simple Interest</option>
                <option value="compound">Compound Interest</option>
            </select>
            <br/>
            <button onClick={calculateInterest} style={styles.button}>Calculate</button>

            {result && <p style={styles.result}>{result}</p>}
        </div>
    );
}
    const styles = {
        container: {
            maxWidth: '400px',
            margin: 'auto',
            padding: '20px',
            border: '1px solid #ddd',
            borderRadius: '8px',
            textAlign: 'center',
            backgroundColor: '#f9f9f9'
        },
        result: {
            marginTop: '10px',
            fontWeight: 'bold',
            color: 'green'
        },
        input: {
            width: '90%',
            padding: '10px',
            margin: '8px 0',
            border: '1px solid #ccc',
            borderRadius: '5px',
            fontSize: '16px'
        },
        button: {
            backgroundColor: '#007BFF', // Blue color
            color: 'white',
            padding: '12px 20px',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
            fontSize: '16px',
            fontWeight: 'bold',
            marginTop: '10px',
            transition: 'background-color 0.3s, transform 0.2s', // Smooth transition
        }
    };
     

export default InterestCalculator;