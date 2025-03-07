import React,{useState} from 'react';

function Increment(){
    const [count,setCount]=useState(0);

    const Value=()=>{
        setCount(count+1);
    };

    return(
        <><p>Count:{count}</p><div>
            <button onClick={Value}>Increment</button>
        </div></>

    );
}
export default Increment;