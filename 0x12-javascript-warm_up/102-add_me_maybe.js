#!/usr/bin/node
exports.addMeMaybe = (number, theFunction) => {
	const addMeMaybe = number + 1;
	theFunction(addMeMaybe);
};
