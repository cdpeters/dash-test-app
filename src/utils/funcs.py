"""Functions used throughout the app.

Functions:
    update_utility_classes
"""
import logging
import re
from typing import Optional

logger = logging.getLogger(__name__)


def update_utility_classes(
    current_classes: str,
    remove_classes: Optional[list[str]] = None,
    add_classes: Optional[list[str]] = None,
    ignore_prefix_warning: bool = False,
) -> str:
    """Update a utility class string by removing and/or adding classes.

    Removes/adds utility classes from/to the `current_classes` string. At least one of
    the arguments `remove_classes` or `add_classes` must be provided. These arguments
    are given in the form of a list of strings representing the classes to be removed or
    added.

    If an incoming add class has a prefix that matches a class(es) in the
    `current_classes` string, a warning will be shown but the add will still be
    completed. The warning is there to make it known that the addition of the class
    could override these prefix matched existing classes in the `current_classes`
    string. The developer should evaluate the add and ensure that this is not the case.
    It is possible that there is no overriding behavior even when there are multiple
    classes with the same prefix. If this is the case, the warning can be suppressed by
    setting the `ignore_prefix_warning` to True.

    Parameters
    ----------
    current_classes : str
        Current utility class string.
    remove_classes : Optional[list[str]], optional
        Classes to be removed, by default None.
    add_classes : Optional[list[str]], optional
        Classes to be added, by default None.
    ignore_prefix_warning : bool, optional
        Flag for suppressing the prefix warning, by default False.

    Returns
    -------
    str
        Updated utility class string.
    """
    # Check if both optional arguments were not provided.
    if remove_classes is None and add_classes is None:
        raise RuntimeError(
            "Both arguments `remove_classes` and `add_classes` were not provided. "
            "Please provide at least one of these arguments."
        )

    current_class_list = current_classes.split()
    # Pattern to match the prefix of a utility class.
    prefix_pattern = r"^-?([a-z:]+)"

    # Remove and/or Add Classes --------------------------------------------------------
    if remove_classes:
        for remove_class in remove_classes:
            try:
                current_class_list.remove(remove_class)
            except ValueError as err:
                raise ValueError(
                    f"The string '{remove_class}', from the `remove_classes` argument, "
                    f"was not found in the `current_classes` string:\n"
                    f"'{current_classes}'"
                ) from err

    if add_classes:
        for add_class in add_classes:
            # Check if the class is already in the `current_class_list`.
            if add_class in current_class_list:
                raise RuntimeError(
                    f"The string '{add_class}', from the `add_classes` argument, is "
                    f"already found within the `current_classes` string:\n"
                    f"'{current_classes}'"
                )

            # Capture the prefix of the incoming add class.
            try:
                prefix = re.search(prefix_pattern, add_class).group(1)
            except AttributeError as err:
                raise RuntimeError(
                    f"The string '{add_class}', from the `add_classes` argument, is "
                    f"not a valid utility class."
                ) from err

            # Capture all classes from `current_classes_list` that match the prefix for
            # the current add class.
            prefix_match_classes = []
            for util_class in current_class_list:
                prefix_match = re.search(prefix, util_class)
                if prefix_match:
                    prefix_match_classes.append(util_class)

            # Warn that there are matches that could result in classes that get
            # overridden by the add. This is a warning and not an error because it is
            # possible to have more than one utility class with the same prefix and not
            # have any overriding behavior.
            if prefix_match_classes:
                if not ignore_prefix_warning:
                    logger.warning(
                        f"WARNING: Upon adding the string '{add_class}', the following "
                        f"class(es) with the same prefix '{prefix}' were found within "
                        f"the `current_classes` string: {prefix_match_classes}\nIf "
                        f"this addition does not result in conflicts, this warning can "
                        f"be suppressed by setting the `ignore_prefix_warning` "
                        f"argument to True.\n"
                    )
            current_class_list.append(add_class)
    return " ".join(current_class_list)
