cube(`Students`, {
  sql: `SELECT student_id, full_name, faculty, group_id FROM student_risk_features`,

  measures: {
    count: {
      type: `count`,
      title: `StudentCount`
    }
  },

  dimensions: {
    studentId: {
      sql: `student_id`,
      type: `number`,
      primaryKey: true
    },

    fullName: {
      sql: `full_name`,
      type: `string`
    },

    faculty: {
      sql: `faculty`,
      type: `string`
    },

    groupId: {
      sql: `group_id`,
      type: `string`
    }
  }
});
