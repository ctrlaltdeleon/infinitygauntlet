// dispatch are sets
// selector are gets
// reducers are manipulation

import React, { Fragment, useState } from "react";

import store, { useSelector } from "redux-toolkit";

export default function reduxToolkit() {
  const endTime = useSelector(selectEndTime);
  const [stateEndTime, setStateEndTime] = useState(endTime);

  return (
    <Fragment>
      <Button onClick={() => setStateEndTime(Data.now())}>
        {stateEndTime}
      </Button>
    </Fragment>
  );
}
